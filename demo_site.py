# importing library.
import streamlit as st




radio = st.sidebar.radio("Your Name", ["About Me", "Experiences", "Skills", "Projects"], index=0)


if radio and radio == "About Me":
    _, dp, _ = st.columns(3)

    with dp:
        st.image("profile_pic.png")

    _, name, _ = st.columns(3)  

    with name:
        st.markdown("# Your Name")

    _, role, _ = st.columns(3) 

    with role:
        st.markdown("### Your current role")

    _, info, _ = st.columns(3) 

    with info:
        st.markdown(" A litte about yourself explaining why you do for which you do.")

    _, _, _, btn1, btn2, btn3, _, _, _ = st.columns(9)

    with btn1:
        st.markdown('''
                    <a href="https://in.linkedin.com/">
                        <img src="https://img.icons8.com/fluency/48/000000/linkedin.png"/>
                    </a>
                    ''', unsafe_allow_html=True)

    with btn2:
        st.markdown('''
                    <a href="https://github.com/">
                        <img src="https://img.icons8.com/fluency/48/000000/github.png"/>
                    </a>
                    ''', unsafe_allow_html=True)

    with btn3:
        st.markdown('''
                    <a href="https://twitter.com/">
                        <img src="https://img.icons8.com/color/48/000000/twitter--v1.png"/>
                    </a>
                    ''', unsafe_allow_html=True)

elif radio and radio == "Experiences":
    
    st.markdown("## Your role")
    st.markdown("#### joing date - leaving date")
    st.text("Descriptions")

    st.markdown("## Your role")
    st.markdown("#### joing date - leaving date")
    st.text("Descriptions")

    st.markdown("## Your role")
    st.markdown("#### joing date - leaving date")
    st.text("Descriptions")

elif radio and radio == "Skills":
    st.markdown("## Programming skills")

    skill1, skill2, skill3, _, _, _ = st.columns(6)

    with skill1:
        st.markdown('<img src="https://img.icons8.com/fluency/48/000000/python.png"/>', unsafe_allow_html=True)

    with skill2:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/javascript--v1.png"/>', unsafe_allow_html=True)

    with skill3:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/c-plus-plus-logo.png"/></br>', unsafe_allow_html=True)

    st.markdown("## Database skills")

    skill1, skill2, skill3, _, _, _ = st.columns(6)

    with skill1:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/mysql-logo.png"/>', unsafe_allow_html=True)

    with skill2:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/postgreesql.png"/>', unsafe_allow_html=True)

    with skill3:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/mongodb.png"/></br>', unsafe_allow_html=True)

    st.markdown("## Deployment skills")

    skill1, skill2, skill3, _, _, _ = st.columns(6)

    with skill1:
        st.markdown('<img src="https://img.icons8.com/fluency/48/000000/docker.png"/>', unsafe_allow_html=True)

    with skill2:
        st.markdown('<img src="https://img.icons8.com/fluency/48/000000/github.png"/>', unsafe_allow_html=True)

    with skill3:
        st.markdown('<img src="https://img.icons8.com/color/48/000000/amazon-web-services.png"/></br>', unsafe_allow_html=True)

elif radio and radio == "Projects":

    st.markdown("## Project title 1")
    st.markdown("#### Project Scope")
    st.text("Description about project")
    st.markdown('''source code: 
                <a href="https://github.com/">
                    <img src="https://img.icons8.com/fluency/48/000000/github.png" width="25" height="25"/>
                </a></br>
                ''', unsafe_allow_html=True)

    st.markdown("## Project title 2")
    st.markdown("#### Project Scope")
    st.text("Description about project")
    st.markdown('''source code: 
                <a href="https://github.com/">
                    <img src="https://img.icons8.com/fluency/48/000000/github.png" width="25" height="25"/>
                </a></br>
                ''', unsafe_allow_html=True)

    st.markdown("## Project title 3")
    st.markdown("#### Project Scope")
    st.text("Description about project")
    st.markdown('''source code: 
                <a href="https://github.com/">
                    <img src="https://img.icons8.com/fluency/48/000000/github.png" width="25" height="25"/>
                </a></br>
                ''', unsafe_allow_html=True)