import streamlit_authenticator as stauth
import streamlit as st

st.title("🔐 Генератор хешированных паролей")

# Поле ввода для паролей
password_input = st.text_input("Введите пароли через запятую:", "123456,qwerty,password")

if st.button("Сгенерировать хеши"):
    # Разбиваем строку на список паролей
    passwords = [p.strip() for p in password_input.split(",") if p.strip()]
    
    # Генерация хешированных паролей
    hashed_passwords = stauth.Hasher(passwords).generate()
    
    # Вывод результатов
    st.subheader("Хешированные пароли:")
    for i, (password, hashed) in enumerate(zip(passwords, hashed_passwords)):
        st.code(f"Пароль: {password}\nХеш: {hashed}", language="text")
    
    st.info("Скопируйте хеши в файл config.yaml")
