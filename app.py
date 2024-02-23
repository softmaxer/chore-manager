import streamlit as st

st.set_page_config(page_title="Epi d'or")
page_bg_img = """
<style>
.st-emotion-cache-uf99v8{
background-image: url("https://i.pinimg.com/originals/0a/5b/e5/0a5be55472c3931b8db224b35cc0c6ce.jpg");
background-size: cover;
}
.st-emotion-cache-18ni7ap{
background: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

heading = """
<h1 style='text-align: center;'> 32 Rue de l'épi d'or </h1>
"""
st.markdown(heading, unsafe_allow_html=True)

names = ["Nassim", "Nirmala", "Kawtar", "Sriram"]


if "current_toil_turn" not in st.session_state:
    st.session_state["current_toil_turn"] = ""

if "current_trash_turn" not in st.session_state:
    st.session_state["current_trash_turn"] = ""

if "next_toil_turn" not in st.session_state:
    st.session_state["next_toil_turn"] = ""

if "next_trash_turn" not in st.session_state:
    st.session_state["next_trash_turn"] = ""


name_select_title = """
<h3 style='text-align: center;'> Please select your name </h3>
"""
st.markdown(name_select_title, unsafe_allow_html=True)
selected_name = st.selectbox("Choose your name:", names, label_visibility="collapsed")

if st.button("I bought the toileteries"):
    current_toil_heading = "### :green[{name}] bought the toileteries".format(
        name=selected_name
    )
    st.session_state.current_toil_turn = selected_name
    # st.markdown(current_toil_heading)
    curr_index = names.index(selected_name)
    next_index = curr_index + 1
    next_index = next_index % len(names)
    next_toil_heading = "### :green[{name}], it's your turn next!".format(
        name=names[next_index]
    )
    st.session_state.next_toil_turn = names[next_index]
    # st.markdown(next_toil_heading)


if st.button("I changed the trash"):
    current_turn_heading = "### :green[{name}] changed the trash".format(
        name=selected_name
    )
    st.session_state.current_trash_turn = selected_name
    # st.markdown(current_turn_heading)
    curr_index = names.index(selected_name)
    next_index = curr_index + 1
    next_index = next_index % len(names)
    next_turn_heading = "### :green[{name}], it's your turn next!".format(
        name=names[next_index]
    )
    st.session_state.next_trash_turn = names[next_index]
    # st.markdown(next_turn_heading)


toileteries, trash = st.columns(2, gap="large")

with toileteries:
    if (
        st.session_state.current_toil_turn != ""
        and st.session_state.next_toil_turn != ""
    ):
        st.markdown(
            "## :green[{name}] last bought the toileteries.\n ## :green[{next_name}], it's your turn next!".format(
                name=st.session_state.current_toil_turn,
                next_name=st.session_state.next_toil_turn,
            )
        )

with trash:
    if (
        st.session_state.current_trash_turn != ""
        and st.session_state.next_trash_turn != ""
    ):
        st.markdown(
            "## :green[{name}] last changed the trash.\n ## :green[{next_name}], it's your turn next!".format(
                name=st.session_state.current_trash_turn,
                next_name=st.session_state.next_trash_turn,
            )
        )
