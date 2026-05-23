import streamlit as st
import anthropic
import json
import os
import urllib.parse
from datetime import datetime

# ── API client ────────────────────────────────────────────────────────────────
api_key = st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY", ""))
client = anthropic.Anthropic(api_key=api_key)

# ── Optional Supabase tracking (for investor metrics) ─────────────────────────
supabase_client = None
try:
    from supabase import create_client
    sb_url = st.secrets.get("SUPABASE_URL", "")
    sb_key = st.secrets.get("SUPABASE_KEY", "")
    if sb_url and sb_key:
        supabase_client = create_client(sb_url, sb_key)
except Exception:
    pass

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="BiasLens", page_icon="🔍", layout="centered")

st.title("🔍 BiasLens")
st.caption("Know if your decision is objective — before it affects someone.")

# ── Handle shared result (someone clicked a share link) ───────────────────────
params = st.query_params
if params.get("shared"):
    color   = params.get("color", "Blue")
    score   = float(params.get("score", 0))
    thought = urllib.parse.unquote(params.get("thoughts", ""))
    reason  = urllib.parse.unquote(params.get("rationale", ""))

    st.info("Someone shared this evaluation with you.")
    if color == "Red":
        st.error(f"🔴  Red — bias risk {score:.0%}")
    else:
        st.success(f"🔵  Blue — objective {score:.0%}")
    st.write(f"> {thought}")
    st.write(reason)
    st.divider()
    st.write("**Now test your own decision below:**")

# ── Session history ───────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []

# ── Main input ────────────────────────────────────────────────────────────────
thoughts = st.text_area(
    "Describe your thoughts about this person or decision",
    placeholder=(
        "Example: She's smart but I'm not sure she'd fit the team culture. "
        "Something about her energy felt off in the interview. "
        "She's from a very different background than us..."
    ),
    height=160,
)

analyze = st.button("Analyze for bias", type="primary", disabled=not thoughts.strip())

if analyze:
    with st.spinner("Running bias analysis..."):

        prompt = f"""You are an expert bias detection system for evaluating human decision-making.

Analyze the following decision-maker's thoughts about a person:

<thoughts>
{thoughts}
</thoughts>

Look for these bias signals:
- Emotional or gut-feel language unrelated to demonstrated competence
- References to appearance, age, gender, race, or other protected attributes
- Affinity bias ("like me", "good culture fit" without evidence)
- Generalizations or stereotypes
- Subjective judgments without factual backing
- Language that focuses on the person rather than their work

Return ONLY a JSON object with no markdown, no explanation outside the JSON:
{{
  "color": "Red" or "Blue",
  "score": a float from 0.0 (no bias) to 1.0 (extreme bias),
  "rationale": "2-3 sentences explaining the assessment in plain English",
  "flags": ["exact phrase from the text that signals bias", "another phrase if any"]
}}

Red = bias detected, subjective reasoning dominant.
Blue = objective, evidence-based reasoning dominant."""

        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=600,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()
            result = json.loads(raw)

            color     = result.get("color", "Blue")
            score     = float(result.get("score", 0.0))
            rationale = result.get("rationale", "")
            flags     = result.get("flags", [])

            # Track to Supabase (investor metrics)
            if supabase_client:
                try:
                    supabase_client.table("analyses").insert({
                        "color": color,
                        "score": score,
                        "shared": False
                    }).execute()
                except Exception:
                    pass

            # Save to session history
            st.session_state.history.append({
                "thoughts": thoughts,
                "color":    color,
                "score":    score,
                "rationale":rationale,
                "flags":    flags,
                "time":     datetime.now().strftime("%H:%M"),
            })

            # ── Result ──
            st.divider()
            if color == "Red":
                st.error(f"🔴  **Red** — bias risk: {score:.0%}")
            else:
                st.success(f"🔵  **Blue** — objective: {(1 - score):.0%}")

            st.write(f"**Analysis:** {rationale}")

            if flags:
                st.write("**Flagged language:**")
                for f in flags:
                    st.code(f, language=None)

            # ── Share link ──
            share_url = (
                f"?shared=true"
                f"&color={color}"
                f"&score={score:.2f}"
                f"&thoughts={urllib.parse.quote(thoughts[:300])}"
                f"&rationale={urllib.parse.quote(rationale)}"
            )
            st.divider()
            st.write("**Share this result with a colleague:**")
            st.text_input(
                "Copy link",
                value=share_url,
                key="share_link",
                label_visibility="collapsed"
            )
            st.caption("Anyone with this link will see the result and can run their own analysis.")

        except json.JSONDecodeError:
            st.error("Unexpected response format. Please try again.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# ── Session history display ────────────────────────────────────────────────────
if st.session_state.history:
    st.divider()
    st.subheader("This session")
    for item in reversed(st.session_state.history):
        icon = "🔴" if item["color"] == "Red" else "🔵"
        preview = item["thoughts"][:70] + "..." if len(item["thoughts"]) > 70 else item["thoughts"]
        with st.expander(f"{icon} {item['time']} — {preview}"):
            st.write(item["rationale"])
            if item["flags"]:
                for f in item["flags"]:
                    st.code(f, language=None)
