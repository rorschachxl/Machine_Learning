import random
import csv
from faker import Faker


fake = Faker('es_ES')


spam_subjects = [
    "¡Gana dinero rápido!", "OFERTA exclusiva solo hoy", "Haz clic aquí para reclamar tu premio",
    "Viagra barato", "Trabajo desde casa y gana $$$"
]
ham_subjects = [
    "Reunión de trabajo", "Tareas pendientes", "Invitación a cumpleaños",
    "Reporte semanal", "Confirmación de cita médica"
]


adjuntos = ["Ninguno", "PDF", "ZIP", "EXE", "DOCX"]

# Abrimos el archivo CSV para guardar
with open("correos_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # Encabezados
    writer.writerow([
        "remitente", "destinatario", "asunto", "fecha_envio", "tamano",
        "num_destinatarios", "contenido", "num_enlaces", "adjunto", "etiqueta"
    ])
    
    # Generar 1000 correos
    for _ in range(1000):
        # Elegimos si será spam o ham
        etiqueta = random.choice(["spam", "ham"])
        
        # Datos comunes
        remitente = fake.email()
        destinatario = fake.email()
        fecha_envio = fake.date_time_this_year()
        tamano = random.randint(5, 500)  # tamaño en KB
        num_destinatarios = random.randint(1, 5)
        
        if etiqueta == "spam":
            asunto = random.choice(spam_subjects)
            contenido = " ".join(fake.words(random.randint(5,15))) + " " + random.choice(["haz clic aquí", "oferta limitada", "reclama ya"])
            num_enlaces = random.randint(1, 5)
            adjunto = random.choice(adjuntos[1:])  # adjuntos sospechosos
        else:
            asunto = random.choice(ham_subjects)
            contenido = " ".join(fake.sentences(random.randint(2,5)))
            num_enlaces = random.randint(0, 1)
            adjunto = random.choice(["Ninguno", "PDF", "DOCX"])
        
        # Escribimos la fila
        writer.writerow([
            remitente, destinatario, asunto, fecha_envio, tamano,
            num_destinatarios, contenido, num_enlaces, adjunto, etiqueta
        ])

print("✅ Dataset generado en 'correos_dataset.csv'")
