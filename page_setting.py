"""General page settings used in app."""
import streamlit as st

class PageSetting:
    """Apply the default layout and options for a domain page.

    Parameters
    ----------
    page_title
      Title we want to use as tab name.
    """
    
    def __init__(
        self,
        page_title: str | None = None,
    ):
        """Glue init args to instance."""
        self.page_title = page_title or ""

    @staticmethod
    def set_page_config(page_title: str):
        """Set the page title, icon and layout."""
        st.set_page_config(page_title=page_title, layout="wide")

    @staticmethod
    def render_title(page_title: str):
        """Render title."""
        st.title(page_title)

    def apply_page_layout(self):
        """Apply all elements page layout elements."""
        self.set_page_config(page_title=self.page_title)
        self.render_title(page_title=self.page_title)
