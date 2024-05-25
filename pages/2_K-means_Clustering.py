import streamlit as st

st.set_page_config(
    page_title="Who are AAC's users by cluster?",
    layout="wide"
)
st.markdown("# Who are AAC's users by cluster?")
# st.sidebar.header("Who are AAC's users by cluster?")
# # st.image("assets/title_slide.png", width = 800)
# st.markdown(
#     """
#     Insert text here in markdown
#     # Heading
#     ## Subheading
#     - Bullets
# """
# )

st.write("## How did we cluster the AAC users?")
st.image("assets/Kcluster - Eugene.png", caption="Cluster Optimization", use_column_width=True)

st.write("## 3D Scatter Plot Labeled by Cluster")
st.image("assets/Kcluster - Eugene (2).png", use_column_width=True)

st.write("## Customer Segmentation based on Demographic Profile and Spending Behavior")
st.image("assets/User Segmentation - Nicole.png", caption="Overview of Customer Segmentation (green text = highest values or unique attributes, orange text = lowest value)", use_column_width=True)

st.write("## Further Generalizations per User Segment ")
st.image("assets/User Segmentation - Nicole (2).png", caption="General Characteristics per User Segment ", use_column_width=True)