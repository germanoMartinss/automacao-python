import asyncio
import os
import subprocess
import tempfile

import edge_tts

VOZ = "pt-BR-FranciscaNeural"  # outras opções: pt-BR-AntonioNeural
TEXTO = "Olá mundo, vamos construir um assistente virtual de voz"


async def falar(texto: str, voz: str = VOZ) -> None:
    comunicador = edge_tts.Communicate(texto, voz)

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as arquivo:
        caminho = arquivo.name

    try:
        await comunicador.save(caminho)
        subprocess.run(["cvlc", "--play-and-exit", caminho], check=True)
    finally:
        os.remove(caminho)


if __name__ == "__main__":
    asyncio.run(falar(TEXTO))
