a
    [�`a�  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZmZmZ e �	� d  Z
dd� ZdZe�  e�  ejZejZejZdd� Zg d�Zdd	� Zd
d� Zdd� Zedkr�z
e�  W n. ey�   eejd ej � e��  Y n0 dS )�    N)�init�Fore�Backc                   C   s*   t dkrt� d� nt dkr&t� d� d S )NZWindows�clsZLinux�clear)�system�os� r	   r	   �port.pyr   
   s    r   z[1;31mc                   C   s   t �d� d S )Nr   )r   r   r	   r	   r	   r
   r      s    (�  �   �   �   �   �   �	   �   �   �   �   �   �   �   �   �   �   �   �    �!   �%   �*   �+   �1   �5   �F   �O   �P   �Q   �R   �S   �T   �U   �X   �Y   �Z   �c   �d   �j   �m   �n   �o   �q   �w   �}   �   �   �   �   �   �   �   �   ��   ��   ��   ��   ��   ��   �   i  i  i  i-  i2  i7  iT  in  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i   i  i  i  i  i  i  i   i!  i$  i*  i+  i3  iK  iQ  ih  ii  iq  iw  i|  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i	  i  i  i   i!  i(  iK  ii  ip  ix  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i   i  i  i  i  i  i  i  i  i	  i
  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i  i   i!  i"  i#  i$  i%  i&  i'  i(  i)  i*  i+  i,  i-  i.  i/  i0  i1  i2  i3  i4  i5  i6  i7  i8  i9  i:  i;  i<  i=  i>  i?  i@  iA  iB  iC  iD  iE  iF  iG  iH  iI  iJ  iK  iL  iN  iP  iQ  iR  iS  iT  iV  iW  iX  iY  iZ  i]  i_  ia  ib  ic  id  if  ij  ik  il  iq  ir  iu  iy  i{  i|  i}  i  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i  i  i  i  i  i  i*  i0  i6  iH  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i,  i/  i:  i@  ii  iz  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i	  i  i  i/  i0  iF  iG  iH  iS  il  iz  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i   i  i  i  i3  i4  i7  i9  i:  i;  i?  iG  iI  iN  iW  i`  ip  iq  iz  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i	  i>	  iM	  iN	  iO	  iY	  iZ	  i_	  ia	  i�	  i�	  i�	  i�	  i�	  i)
  i*
  i,
  i-
  i/
  i0
  iN
  i�
  i�
  i�
  i�
  i�
  i�
  i�
  i�
  i�
  i5  i;  i]  i^  ih  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i8  i`  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i  i'  i)  i*  i+  i,  i=  i>  iL  i�  i�  i�  i�  i�  i�  i�  iK  ii  ij  iw  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i  i  i&  i(  i1  iA  iJ  iN  iP  ii  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i  i  i!  i�  i�  i�  i�  i�  i[  i\  i]  i^  ia  i�  i�  i6  i�  i#  i$  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i   iF  iP  i^  ie  if  ii  ij  i�  i�  i�  i�  i  i&  i7  i8  i@  i|  i�  i�  i�  i�  i�  i�  i�  i  i"  i.  i/  iV  ib  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i  i  i  i  i  i  i  i  i  i  i"  i%  i>  i@  iG  iH  iI  iJ  iK  ic  id  ie  in  io  ip  iq  ir  is  it  iu  iv  iw  iy  i�  i�  i�  i�  i�  i�  i�  i�  i  i�  i�  if  in  i�  i�  i�  i�  i�  i�  i�  i
  i  i  i  i!  i$  i+  i{  i�  i�  i�  i�  i�  i�  i9  iX  iY  iZ  i\  i_  ik  iq  i�  i�  i�  i�  i   i!  i�  i  i  iH  iX  i�  i�  i�  i=  ia  ib  ix  i�  i�  i�  i  i  i?  i@  iA  iB  iG  iH  iI  iJ  iK  iU  iV  i_  ij  im  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i�  i    i   i   i   i   i>   ib   ic   id   il   i�   i�   i�   i�   i�   i4!  i�!  i�!  i�!  i�!  i�!  i�!  i`"  i�"  i�"  i�"  i"#  i(#  i)#  i*#  i+#  i1#  i2#  i3#  iP#  iZ#  io#  ix#  iy#  i�#  i�#  i�#  i�#  i�#  i�#  i�#  i�#  i�#  i�#  i�#  i$  iJ$  i�$  i�$  i%  i%  i%  i%  i?%  ig%  iy%  iz%  i{%  i�%  i�%  i�&  i�&  i�&  i�&  i�&  i�&  i�&  i�&  i�&  i�&  i'  i'  i'  i'  i'  i'  i'  i'  i'  i'  i('  i)'  ib'  i�'  i�'  i(  iF)  ix)  iy)  i})  i�)  i�)  i�)  i*  if+  ig+  i�.  i�.  i�/  i�/  i90  i�4  i�5  i�5  i�5  i�6  i�7  ii8  ij8  i�:  i�:  i�:  i�:  i,=  i~=  i�>  i�>  i�>  i�>  i�>  i�>  i�>  i`B  iaB  i�E  iDF  ixF  i�F  i,J  i�J  iSK  isK  i�K  iDM  iYM  i�M  i N  i%N  i?N  i�N  i�N  i\Q  iCT  i�Y  i�[  i|_  i�`  i�d  i�d  iff  ixi  i�j  i�j  i�j  i�j  iCl  i)n  i0u  i�w  i�x  i>y  iiz  i �  i�  i�  i�  i�  i�  i�  i�  i�  i	�  i
�  i�  i�  i�  i�  i�  i�  i�  iJ�  ik�  i�  i�  i�  i��  i��  i�  iϟ  i'�  i�  i��  i��  i��  iխ  i,�  iл  i �  i�  i�  i�  i�  i�  i�  i�  i�  i	�  i�  i�  i�  i�  i�  i��  iO�  iP�  iQ�  iR�  iS�  iV�  i|�  i��  iD�  i��  ip�  i��  i%�  i��  iV�  ip�  i��  i�  i8�  i�  i�  i�  i0�  i��  i��  i��  i��  i��  it�  i�  i\�  i��  i~�  ic�  io�  i��  i��  ii�  im�  c                 C   s<   t � � }z|�| |f� |�d� W n   Y dS 0 dS d S )Ng�������?FT)�socketZconnectZ
settimeout)�host�port�sr	   r	   r
   �is_port_open   s    rJ   c                   C   s   t tjd tj � d S )Nu�  
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░
             ░ ░     ░                    ░  ░ ░            ░  ░         ░
                                             ░)�printr   �GREEN�RESETr	   r	   r	   r
   �banner*   s    

�rN   c               
   C   s�   t �d� t�  t�  tt� d�� tt� d�� ttt� d���} t�  t�  tt� d�� tt� d�� tt� d��}t�	d� t
d| d �D ]X}t||�r�tdt� d	|� d
|� dt� �dd� q�tdt� d|� d
| � dt� �dd� q�d S )Nzprintf ']2;Port Scan'z[>] Developer: mishakorzikz[>] Version  : v1.1.0z	To port: z
While Ip: r   r   �
z[+] z: z is open      �)�endz[-] z is Filter    )r   r   r   rN   rK   rL   �int�input�time�sleep�rangerJ   rM   �RED)ZnomesrG   rH   r	   r	   r
   �menu7   s     


&rX   �__main__z[+] Keyboard Interrupt! )�platformrT   rF   r   �sysZcoloramar   r   r   �unamer   r   rW   rL   rM   ZLIGHTBLACK_EXZGRAYZTOP_1000_PORTSrJ   rN   rX   �__name__�KeyboardInterruptrK   ZWHITE�exitr	   r	   r	   r
   �<module>   s2   
