
class TV(object):

	def __init__(self, volume, channel, channels):
		self.volume = volume
		self.channel = channels[channel-1]

	def set_channel(self, channel):
		self.channel = channel

	def get_channel(self):
		return self.channel

	def set_volume(self, volume):
		self.volume = volume
	
	def get_volume(self):
		return self.volume