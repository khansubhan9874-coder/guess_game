import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="File Manager by SUBHAN", layout="centered")

st.title("📁 File & Folder Manager")
st.caption("Created by SUBHAN")

BASE_PATH = Path(".")

# ---------- Helper ----------
def list_items():
    return list(BASE_PATH.rglob("*"))

# ---------- Sidebar Menu ----------
menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Folder",
        "List Files & Folders",
        "Rename Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
    ],
)

# ---------- Create Folder ----------
if menu == "Create Folder":
    st.subheader("📂 Create Folder")
    name = st.text_input("Enter folder name")
    if st.button("Create Folder"):
        p = Path(name)
        if not p.exists():
            p.mkdir()
            st.success("Folder created successfully ✅")
        else:
            st.error("Folder already exists ❌")

# ---------- List ----------
elif menu == "List Files & Folders":
    st.subheader("📃 Files & Folders")
    items = list_items()
    if items:
        for i, item in enumerate(items, start=1):
            st.write(f"{i}. {item}")
    else:
        st.info("No files or folders found")

# ---------- Rename Folder ----------
elif menu == "Rename Folder":
    st.subheader("✏️ Rename Folder")
    old = st.text_input("Old folder name")
    new = st.text_input("New folder name")
    if st.button("Rename Folder"):
        old_p = Path(old)
        new_p = Path(new)
        if old_p.exists() and old_p.is_dir():
            if not new_p.exists():
                old_p.rename(new_p)
                st.success("Folder renamed successfully ✅")
            else:
                st.error("New folder name already exists ❌")
        else:
            st.error("Folder not found ❌")

# ---------- Delete Folder ----------
elif menu == "Delete Folder":
    st.subheader("🗑️ Delete Folder")
    name = st.text_input("Folder name to delete")
    if st.button("Delete Folder"):
        p = Path(name)
        if p.exists() and p.is_dir():
            try:
                p.rmdir()
                st.success("Folder deleted successfully ✅")
            except:
                st.error("Folder not empty ❌")
        else:
            st.error("Folder not found ❌")

# ---------- Create File ----------
elif menu == "Create File":
    st.subheader("📄 Create File")
    name = st.text_input("File name with extension")
    content = st.text_area("File content")
    if st.button("Create File"):
        p = Path(name)
        if not p.exists():
            with open(p, "w") as f:
                f.write(content)
            st.success("File created successfully ✅")
        else:
            st.error("File already exists ❌")

# ---------- Read File ----------
elif menu == "Read File":
    st.subheader("📖 Read File")
    name = st.text_input("File name with extension")
    if st.button("Read File"):
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as f:
                st.text_area("File Content", f.read(), height=300)
            st.success("File read successfully ✅")
        else:
            st.error("File not found ❌")

# ---------- Update File ----------
elif menu == "Update File":
    st.subheader("🛠️ Update File")
    name = st.text_input("File name")
    action = st.radio("Select action", ["Rename", "Overwrite", "Append"])

    if action == "Rename":
        new_name = st.text_input("New file name")

    content = st.text_area("Content")

    if st.button("Update File"):
        p = Path(name)
        if p.exists() and p.is_file():
            if action == "Rename":
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    st.success("File renamed successfully ✅")
                else:
                    st.error("File name already exists ❌")

            elif action == "Overwrite":
                with open(p, "w") as f:
                    f.write(content)
                st.success("File overwritten successfully ✅")

            elif action == "Append":
                with open(p, "a") as f:
                    f.write("\n" + content)
                st.success("File appended successfully ✅")
        else:
            st.error("File not found ❌")

# ---------- Delete File ----------
elif menu == "Delete File":
    st.subheader("🗑️ Delete File")
    name = st.text_input("File name")
    if st.button("Delete File"):
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            st.success("File deleted successfully ✅")
        else:
            st.error("File not found ❌")
