o
    �b,  �                   @   s\  d Z edddd��Ze�� Z W d  � n1 sw   Y  i dd�dd	�d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d'�d(d)d*��Zed+�Zed,krmeD ]
Ze �eee �Z qane	e�D ]
Ze �eee �Z qqed-�Z
e
d.ks�e
d/kr�d0�e	e ��Z ed1d2dd��Ze�e � W d  � dS 1 s�w   Y  dS )3� zinput/input.txt�rzutf-8)�encodingN�au   а�cu   с�du   ԁ�eu   е�hu   һ�iu   і�ju   ј�ku   κ�lu   ӏ�nu   ո�ou   о�pu   р�su   𝑠�tu   𝑡�qu   զ�uu   υ�vu   νu   хu   у)�x�yz3what letters do you want to replace (e.g. abc...): �allzneed a DeepClean(y/n): r   �Yu   ‍zoutput/plagiarism-removed.txt�w)�text�open�file�readZunicode_letters�inputZreplaceLettersZletter�replace�listZ	deepClean�join�write� r#   r#   �plagiarismRemover.py�<module>   sv    
���������	�
������������"�