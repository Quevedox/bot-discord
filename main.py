import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

frases_por_nombre = {
  'nombre1': ["frase1","frase2", "frase3"],
  'nombre2': ["frase1","frase2", "frase3"],
  'nombre3': ["frase1","frase2", "frase3"],
  # Agrega más nombres y frases aquí
}

nombres = ["", "", ""]


def mostrar_nombres():
  for nombre in nombres:
    print(nombre)


def handle_help_command():
  print("Los nombres que podes poner son:")
  mostrar_nombres()


def handle_command(command):
  if command == "!help":
    handle_help_command()
  else:
    print("Comando desconocido")


# Ejemplo de uso
handle_command("!help")


@bot.event
async def on_ready():
  print(f'Bot conectado como {bot.user.name}')


@bot.command()
async def tts(ctx, nombre=None):
  if nombre is not None:
    nombre = nombre.lower()  # Convertir a minúsculas
    if nombre in frases_por_nombre:
      frases = frases_por_nombre[nombre]
      frase = random.choice(frases)
      await ctx.send(frase, tts=True)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('!'):
    command = message.content[1:].lower()  # Convertir a minúsculas
    if command in frases_por_nombre:
      frases = frases_por_nombre[command]
      frase = random.choice(frases)
      await message.channel.send(frase)

  await bot.process_commands(message)


bot.run(
  'TOKEN_DEL_BOT')