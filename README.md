# 📡 Trabalho de Monitoramento Pervasivo
- Android (Kivy) → Servidor Python via Socket TCP


# 📖 Descrição

Este projeto implementa um sistema de monitoramento pervasivo, onde um aplicativo Android atua como um nó sensor.

O app coleta informações do dispositivo em tempo real, como:

🔋 Nível de bateria

📍 Localização GPS

Esses dados são enviados via socket TCP para um servidor central desenvolvido em Python, responsável por receber e exibir as informações.


# ⚙️ Tecnologias Utilizadas
🐍 Python
📱 Kivy 2.3.1
🎨 KivyMD 1.1.1
📡 Plyer
🔌 Socket TCP


# 🚀 Como Executar

🔹 Servidor (Python)

1. Execute o servidor:

```python3 server.py```

2. Saida esperada:

```Aguardando dados dos sensores... 0.0.0.0:50007```

## 📦 Download do APK

Você pode baixar e testar o aplicativo diretamente:

👉 [Clique aqui para baixar o APK](./myapp-0.1-arm64-v8a_armeabi-v7a-debug.apk)

> ⚠️ Pode ser necessário ativar "Instalar apps de fontes desconhecidas" no Android.
> ⚠️ É necessário ativar a permissão de localização.



# 📸 Interface
 ![WhatsApp Image 2026-03-24 at 17 05 01](https://github.com/user-attachments/assets/76918507-f6fc-421c-ad27-0692c18229a3)


# Log
![WhatsApp Image 2026-03-24 at 17 47 36](https://github.com/user-attachments/assets/aaac8f9d-28fe-477b-9153-e1f76ce19191)



