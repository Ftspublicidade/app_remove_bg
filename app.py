import streamlit as st
from rembg import remove
from PIL import Image
import io

def remove_background(input_img):
    inp = Image.open(input_img)
    output = remove(inp)
    return output

def main():
    st.set_page_config(layout="wide")

    st.image("f3.png", width=100)
    st.title("Remover Fundo de Imagem")

    uploaded_file = st.file_uploader("Faça o upload de uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem original", use_column_width=True)

        if st.button("Remover Fundo"):
            with st.spinner("Removendo o fundo..."):
                output_img = remove_background(uploaded_file)
                st.image(output_img, caption="Imagem com fundo removido", use_column_width=True)
                st.success("Fundo removido com sucesso!")

                # Download automático da imagem com fundo removido
                img_bytes = io.BytesIO()
                output_img.save(img_bytes, format='PNG')
                st.download_button(label="Baixar Imagem com Fundo Removido", data=img_bytes, file_name="imagem_sem_fundo.png", key="download_button")

if __name__ == "__main__":
    main()
