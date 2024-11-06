import streamlit as st
from page_setting import PageSetting

# Set page configuration
PAGE_SETTING = PageSetting(
    page_title="Home"
)

def main():
    pass

if __name__ == "__main__":
    PAGE_SETTING.apply_page_layout()
    main()