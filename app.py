import streamlit as st
from gmail_connect import authenticate_gmail
from email_fetcher import get_unread_emails
from summarizer import summarize_text
from gmail_connect import generate_reply  # Import generate_reply function

st.set_page_config(page_title="Smart Email Assistant", layout="wide")
st.title("📧 Smart Email Assistant (Free Version)")
st.write("Fetch your unread Gmail messages, get smart summaries, and auto-generate replies!")

# Button to connect Gmail
if st.button("🔐 Connect to Gmail"):
    service = authenticate_gmail()
    st.success("✅ Gmail connected successfully!")

    emails = get_unread_emails(service)

    if emails:
        for idx, email in enumerate(emails):
            st.subheader(f"📩 Email #{idx + 1}")
            st.write(f"**From:** {email['from']}")
            st.write(f"**Subject:** {email['subject']}")
            st.write(f"**Body Preview:** {email['body'][:300]}...")

            # Summarize the email
            if st.button(f"Summarize Email #{idx + 1}", key=f"summary_{idx}"):
                summary = summarize_text(email['body'])
                st.success(f"🧠 Summary:\n{summary}")

            # Generate a formal reply
            user_input = st.text_area(f"🔄 Enter your brief reply for Email #{idx + 1}", key=f"input_{idx}")

            if user_input:
                if st.button(f"Generate Formal Reply for Email #{idx + 1}", key=f"generate_{idx}"):
                    generated_email = generate_reply(user_input)
                    
                    # Display Subject and Body separately
                    subject = generated_email.split('\n')[0].replace('**Subject:** ', '')
                    body = '\n'.join(generated_email.split('\n')[1:])
                    
                    st.subheader("📝 Generated Subject:")
                    st.write(subject)
                    st.markdown("---")
                    st.subheader("📝 Generated Email Body:")
                    st.write(body)

                    # Add a "Copy" button for both subject and body
                    if st.button(f"Copy Subject for Email #{idx + 1}", key=f"copy_subject_{idx}"):
                        st.write("**Subject copied!**")
                        st.text(subject)  # Will display text for the user to copy

                    if st.button(f"Copy Body for Email #{idx + 1}", key=f"copy_body_{idx}"):
                        st.write("**Body copied!**")
                        st.text(body)  # Will display text for the user to copy

    else:
        st.info("No unread emails found.")
else:
    st.warning("Click the button above to connect your Gmail.")
