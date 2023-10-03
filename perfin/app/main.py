import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from perfin.agent import DB_CHAIN, PROMPT
from perfin.app.auth import authenticate
from perfin.app.ui.sidebar import init_sidebar

# st.set_page_config(page_title="Perfin: Personal Finance Assistant", page_icon="💸")


def main():
    if user := authenticate():
        init_sidebar(user.name)

        st_cb = StreamlitCallbackHandler(st.container())

        if "messages" not in st.session_state or st.sidebar.button(
            "Clear message history", use_container_width=True
        ):
            st.session_state["messages"] = [
                {"role": "assistant", "content": "How can I help you?"}
            ]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if user_query := st.chat_input(placeholder="Ask me anything!"):
            st.session_state.messages.append({"role": "user", "content": user_query})
            st.chat_message("user").write(user_query)

            with st.chat_message("assistant"):
                prompt = PROMPT.format(
                    query=user_query,
                    user=user.username,
                    table="transactions",
                    table_columns=f'{["user_key", "date", "text", "category", "subcategory", "amount", "balance"]}',
                    dialect="sqlite",
                )

                response = DB_CHAIN.run(prompt, callbacks=[st_cb])

                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)


if __name__ == "__main__":
    # st.set_page_config(
    #     page_icon= "💰",
    #     page_title= "Perfin - Personal Finance",
    #     layout= "wide",
    #     initial_sidebar_state= "expanded",
    #     menu_items= {
    #         'Get Help': 'https://www.github.com/nthomsencph/perfin',
    #         'Report a bug': "https://www.github.com/nthomsencph/perfin/issues",
    #         'About': "# Personal finance made easy. Perfin enables you to track your expenses and income, and visualize your spending habits."
    #     }
    # )
    main()
