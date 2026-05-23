import streamlit as st
from groq import Groq
import json

st.set_page_config(page_title="BiasLens", page_icon="🔍", layout="centered")

client = Groq(api_key="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")

st.title("🔍 BiasLens")
st.caption("Know if your decision is objective — before it affects someone.")

if "history" not in st.session_state:
    st.session_state.history = []

thoughts = st.text_area("Describe your thoughts about this person or decision",
    placeholder="She's smart but I'm not sure she'd fit the team culture...",
    height=160)

analyze = st.button("Analyze for bias", type="primary", disabled=not thoughts.strip())

if analyze:
    with st.spinner("Analyzing..."):
        prompt = f"""You are a bias detection system. Analyze this text for cognitive bias:

"{thoughts}"

Return ONLY valid JSON:
{{"color": "Red" or "Blue", "score": 0.0 to 1.0, "rationale": "2-3 sentences", "flags": ["phrase1", "phrase2"]}}

Red = bias detected. Blue = objective reasoning."""

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=400,
                response_format={"type": "json_object"}
            )
            result = json.loads(response.choices[0].message.content)
            color = result.get("color", "Blue")
            score = float(result.get("score", 0.0))
            rationale = result.get("rationale", "")
            flags = result.get("flags", [])

            st.divider()
            if color == "Red":
                st.error(f"🔴 RED — Bias detected ({score:.0%})")
            else:
                st.success(f"🔵 BLUE — Objective reasoning ({(1-score):.0%})")

            st.write(f"**Analysis:** {rationale}")
            if flags:
                st.write("**Flagged language:**")
                for f in flags:
                    st.code(f, language=None)

        except Exception as e:
            st.error(f"Error: {str(e)}")