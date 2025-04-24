import streamlit as st
import re

st.markdown("<h1 style='text-indent: 60px;'>Welcome!</h1>", unsafe_allow_html=True)
st.title("🚀The Password Strength Meter")

st.markdown("""
It's the **Ultimate Password Strength Meter**!
            
To keep your account protected, make sure your password includes:
            
- ➡️ Length
- ➡️ Case Sensitivity
- ➡️ Numbers
- ➡️ Special Characters
 """)

password = st.text_input("Enter Your Password" , type = "password")

def password_strength (password):
    percent = 0 
    feedback = []


    if len(password) >= 8:
        percent += 25
    else :
        feedback.append ("Your password is weak! Write atleast **8 Characters**.")


    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
       percent += 25
    else:
        feedback.append ("Your password is weak! Write both **Uppercase and Lowercase letters**.")


    if re.search(r"[0-9]", password):
        percent += 25
    else:
        feedback.append ("Your password is weak! Write atleast **One Number**.")


    if re.search(r"[!@#$%^&*]", password):
       percent += 25
    else:
        feedback.append ("Your password is weak! Add atleast **One Special Character**.")
    
    return percent, feedback

if st.button("💪🏼Check the password strength."):
    if password:
        percent, feedback= password_strength(password)

        st.subheader("Password strength result is:")

        if percent == 100:
            st.success("✔️Your Password is strong and secure!")
        elif percent == 50:
            st.warning("⚠️Your password is neither strong nor weak! Make it stong by adding more features.")
        else:
            st.error("❌Your password is weak!")


        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write(tip)
        else:
            st.success("No Suggestions!")
