import streamlit as st
import json

with open("info.json", "r") as f:
    local_session_state = json.load(f)

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


name_select_title = """
<h3 style='text-align: center;'> Please select your name </h3>
"""
st.markdown(name_select_title, unsafe_allow_html=True)
selected_name = st.selectbox("Choose your name:", names, label_visibility="collapsed")

# Columns
col1, col2, col3, col4 = st.columns(4, gap="large")
with col1:
    if st.button("I bought the dish soap"):
        current_toil_heading = "### :green[{name}] bought the dish soap".format(
            name=selected_name
        )
        local_session_state["dish_soap"]["current"] = selected_name
        # st.markdown(current_toil_heading)
        curr_index = names.index(selected_name)
        next_index = curr_index + 1
        next_index = next_index % len(names)
        next_toil_heading = "### :green[{name}], it's your turn next!".format(
            name=names[next_index]
        )
        local_session_state["dish_soap"]["next"] = names[next_index]
        with open("info.json", "w") as f:
            json.dump(local_session_state, f)
        # st.markdown(next_toil_heading)


with col2:
    if st.button("I changed the trash"):
        current_turn_heading = "### :green[{name}] changed the trash".format(
            name=selected_name
        )
        local_session_state["trash"]["current"] = selected_name
        # st.markdown(current_turn_heading)
        curr_index = names.index(selected_name)
        next_index = curr_index + 1
        next_index = next_index % len(names)
        next_turn_heading = "### :green[{name}], it's your turn next!".format(
            name=names[next_index]
        )
        local_session_state["trash"]["next"] = names[next_index]
        with open("info.json", "w") as f:
            json.dump(local_session_state, f)
        # st.markdown(next_turn_heading)

with col3:
    if st.button("I bought the toilet paper"):
        ctp = "### :green[{name}] bought the toilet paper".format(name=selected_name)
        local_session_state["toilet_paper"]["current"] = selected_name
        curr_index = names.index(selected_name)
        next_index = curr_index + 1
        next_index = next_index % len(names)
        next_turn_heading = "### :green[{name}], it's your turn next!".format(
            name=names[next_index]
        )
        local_session_state["toilet_paper"]["next"] = names[next_index]
        with open("info.json", "w") as f:
            json.dump(local_session_state, f)


with col4:
    if st.button("I bought the Handwash"):
        ctp = "### :green[{name}] bought the Hand wash".format(name=selected_name)
        local_session_state["hand_wash"]["current"] = selected_name
        curr_index = names.index(selected_name)
        next_index = curr_index + 1
        next_index = next_index % len(names)
        next_turn_heading = "### :green[{name}], it's your turn next!".format(
            name=names[next_index]
        )
        local_session_state["hand_wash"]["next"] = names[next_index]
        with open("info.json", "w") as f:
            json.dump(local_session_state, f)

st.divider()
d1, d2, d3, d4 = st.columns(4, gap="large")

with d1:
    if (
        local_session_state["dish_soap"]["current"] != ""
        and local_session_state["dish_soap"]["next"] != ""
    ):
        st.markdown(
            "## :green[{name}] last bought the dish soap.\n ## :green[{next_name}], it's your turn next!".format(
                name=local_session_state["dish_soap"]["current"],
                next_name=local_session_state["dish_soap"]["next"],
            )
        )


with d2:
    if (
        local_session_state["trash"]["current"] != ""
        and local_session_state["trash"]["next"] != ""
    ):
        st.markdown(
            "## :green[{name}] last changed the trash.\n ## :green[{next_name}], it's your turn next!".format(
                name=local_session_state["trash"]["current"],
                next_name=local_session_state["trash"]["next"],
            )
        )


with d3:
    if (
        local_session_state["toilet_paper"]["current"] != ""
        and local_session_state["toilet_paper"]["next"] != ""
    ):
        st.markdown(
            "## :green[{name}] last bought the toilet paper.\n ## :green[{next_name}], it's your turn next!".format(
                name=local_session_state["toilet_paper"]["current"],
                next_name=local_session_state["toilet_paper"]["next"],
            )
        )


with d4:
    if (
        local_session_state["hand_wash"]["current"] != ""
        and local_session_state["hand_wash"]["next"] != ""
    ):
        st.markdown(
            "## :green[{name}] last bought the hand wash.\n ## :green[{next_name}], it's your turn next!".format(
                name=local_session_state["hand_wash"]["current"],
                next_name=local_session_state["hand_wash"]["next"],
            )
        )
