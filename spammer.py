U
    N��^  �                   @   s|   d dl Z d dlZd dlmZ dZdZdZdZdZdZ	d	Z
d
ZdZdZdZdZdd� Zdd� Zdd� Zdd� Ze�  e�  dS )�    N)�systemz[30mz[22;31mz[1;31mz[32mz[1;32mz[1;33mz[34mz[1;34mz[35mz[36mz[37mz[0mc                   C   sx   t d� ttd t d t d t d t d d t d t d t d	 t d t d
 t d t d t � d S )N�clearat  
                                                      
                  :.                   i              
                 LBRBB.             :BBBR.            
               .QQBBBBQBQi       7BQBQBQBBQ           
                BBBBQBBBBQQRi:BQBQBBBBBBQBi           
               .  QQBQBQRBBQQBBBQBQBQBBBB :.          
              7BQB BRBRBBQBRBQQBQBQBBBQ  BBB          
              vBBBQBQBBBBBQRQRBBBBBBQBBQBBBR.         
               QBBBBBBRBBBQBBQBBQBRQQBQBQQQQ          
               BQR  iBQBBBQQBBBBBBQQBB. QRBB          
             rBQBBQ   RBBBBBBBQBBBBQi  lBBQQ.        
              BBQQQi   �#ZBBBQQBBBQBQz	   BBQBRraF          
                BBQBBQ.   QBBBBQB   .QBBBB.           
            vB    BBQBQRBQBQBBRBBQBRBBBBB    Br       
         .QBQQQBB. :QBBBQBQBB RBQBQBQBR  BBBBBBQB     
        QQQBBB.QBQ.  BQBQ:BB  .BBQBBBi  BBBBQBQBQBv   
       QQBQQBQBB BB   :B  QB   BB .Q   .QB.BRBBBRQBv  
       iBBBQBQBBBBQi     QB  B rB:     7BBQBBBBBBQB.  
        LB:QBBQBQB        QBBBQQr        QRBBBQBBB:   
         :BiBRBR.           BQi           iBBBBB7.    
            . :                             i.        
                   MULTI-SPAMMER404 v1.0
                       BY KEVIN(Kv7)
z
           WHATSAPP�-ZFACEBOOKZ	INSTAGRAMz	TELEGRAM
)r   �print�red�gold�greenn�bluee�redb�reset� r   r   �3/home/kv7/PycharmProjects/untitled/spammerpy/run.py�banner   sd    ������������������������r   c                  C   s�   t ttd t d t ��} ttd t d t dd� t� }tttd t d t ��}ttd t � t�	d� d	}|| kr�t�	|� t
�|� t
�d
� |d	 }|| krxttd t � t�  qxd S )N�Cantidad de mensajes�-->zMensaje a spammear� ��end�Velocidad de spamm�A
Tendras 4s para posicionar el cursor luego de presionar enter...�   �   �enter�FIN!!!��int�input�greenr   r   r   �floatr   �time�sleep�keyboard�write�send�exit)�mensajes�msg�tiempo�ir   r   r   �spamm13   s    



r*   c                  C   s   t ttd t d t ��} ttd t d t dd� t� }ttd t d t dd� t� }tttd t d t ��}ttd t � t�	d	� d
}|| kr�t�	|� t
�|� t
�d� t
�|� t
�d� |d
 }|| kr�ttd t � t�  q�d S )Nr   r   zPrimer mensaje a spammearr   r   zSegundo mensaje a spammearr   r   r   r   r   r   r   )r&   Zmsg1Zmsg2r(   r)   r   r   r   �spamm2H   s&    





r+   c                  C   s^   t td � ttd t d t �} | dkr4t�  n&| dkrDt�  nt td t � t�  d S )Nz!
1-Spamm MSGx1
2-Spamm MSGx2
    zSeleccione una opcionr   �1�2z*Opcion no encontrada ERROR404 NOT FOUND!!!)	r   r   r   r   r   r*   r+   r   �opciones)Zopcr   r   r   r.   b   s    r.   )r"   r    �osr   Zblackr   r   r   r	   r   Zbluer
   ZmagentaZcyanZwhiter   r   r*   r+   r.   r   r   r   r   �<module>   s(   