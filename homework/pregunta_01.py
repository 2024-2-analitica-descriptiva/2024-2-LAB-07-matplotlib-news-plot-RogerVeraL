"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    def cargar_datos(directorio_entrada):
        for archivo in glob.glob(os.path.join(directorio_entrada, "*.csv")):
            return pd.read_csv(archivo, sep=",", index_col=0)

    def graficar(df, directorio_salida, nombre_archivo):
        plt.figure()
        plt.title('How people get their news', fontsize = 16)

        #quitar bordes
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
    

        colores = {
            'Television': 'dimgray',
            'Radio': 'lightgray',
            'Internet': 'tab:blue',
            'Newspaper': 'grey'
        }

        posicion = {
            'Television': 1,
            'Radio': 1,
            'Internet': 2,
            'Newspaper': 1
        }

        ancho = {
            'Television': 1.5,
            'Radio': 1.5,
            'Internet': 3,
            'Newspaper': 1.5
        }

        for col in df.columns:
            #lineas
            plt.plot(
                df[col],
                color=colores[col],
                label=col,
                zorder = posicion[col],
                linewidth = ancho[col]
                )
            
            #puntos
            primer_valor = df.index[0]
            plt.scatter(
                x = primer_valor,
                y = df[col][primer_valor],
                color = colores[col],
                )
            ultimo_valor = df.index[-1]
            plt.scatter(
                x = ultimo_valor,
                y = df[col][ultimo_valor],
                color = colores[col],
                )
            
            #etiquetas
            plt.text(
                x = primer_valor-0.2,
                y = df[col][primer_valor],
                s = col + ' ' + str(df[col][primer_valor]) + '%',
                color = colores[col],
                ha = 'right',
                va = 'center'
            )
            plt.text(
                x = ultimo_valor+0.2,
                y = df[col][ultimo_valor],
                s = str(df[col][ultimo_valor]) + '%',
                color = colores[col],
                ha = 'left',
                va = 'center'
            )
        plt.xticks(
            ticks = df.index,
            labels = df.index,
            ha = 'center'
        )

        plt.legend(loc='upper right')

        #guardar
        if not os.path.exists(directorio_salida):
            os.makedirs(directorio_salida)
        plt.tight_layout()
        plt.savefig(os.path.join(directorio_salida, nombre_archivo))
        plt.close()

    directorio_entrada = "files/input"
    directorio_salida = "files/plots"
    nombre_archivo = "news.png"

    df = cargar_datos(directorio_entrada)
    graficar(df, directorio_salida, nombre_archivo)

pregunta_01()