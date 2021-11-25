import numpy as np
import random


class Wave:

	def __init__(self, label, signal):
		self.label = label
		self.signal = signal
		self.tx = 2
		self.amp = sum(self.signal) / len(self.signal)

	def __repr__(self):
		print("O sinal {} possui {} de amplitude e {} de taxa de gravação. O sinal é {}{}".format(self.label, self.amp, self.tx, self.signal,"\n"))


	def __add__(self, onda):
		new_signal = np.add(self.signal, onda.signal)
		new_label = '{} + {}'.format(self.label, onda.label)
 		return Wave(new_label, new_signal)
  
	def __sub__(self, onda):
		new_signal = np.subtract(self.signal, onda.signal)
		new_label = '{} - {}'.format(self.label, onda.label)
		return Wave(new_label, new_signal)

	def __mul__(self, onda):
		new_signal = np.concatenate((self.signal, onda.signal))
		new_label = '{} * {}'.format(self.label, onda.label)
		return Wave(new_label, new_signal)

	def __gt__(self, onda):
		if self.amp > onda.amp:
			return True
  
	def __lt__(self, onda):
		if self.amp < onda.amp:
			return True
  
	def __eq__(self, onda):
		if self.amp == onda.amp:
			return True
    
	def __ne__(self, onda):
		if self.amp != onda.amp:
			return True
  
	def __getitem__(self, index):
		mm = list(self.waves)
		self.waves = mm[index]
		return self

def main():

	w1 = Wave(label='w1', signal=np.random.normal(-1, 1, size=50))
	w2 = Wave(label='w2', signal=np.random.normal(-1, 1, size=50))
 	w3 = Wave(label='w3', signal=np.random.normal(-1, 1, size=50))
 	w4 = Wave(label='w4', signal=np.random.normal(-1, 1, size=50))
 	w5 = Wave(label='w5', signal=np.random.normal(-1, 1, size=50))

	print(w1 + w4)
	print(w3 - w5)
	print(w2 * w1)

	lista_ondas = [w1, w2, w3, w4, w5]
	maior_amp = w1
	menor_amp = w1

	for onda in lista_ondas:
		if onda > maior_amp:
			maior_amp = onda
    
		if onda < menor_amp:
			menor_amp = onda
    
		if onda == maior_amp:
			print('Os sinais {} e {} têm a mesma amplitude média'.format(onda.label, maior_amp.label))
  
	print('{} possui a maior amplitude média'.format(maior_amp.label))
	print('{} possui a menor amplitude média'.format(menor_amp.label))
	print(maior_amp)
	print(menor_amp)

main()


