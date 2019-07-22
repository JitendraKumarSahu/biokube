from abc import ABC, abstractmethod

class Cloud(ABC):
	'''Abstract class for creating cloud infrastructure'''
	
	# abstract method
	def create_cluster(self):
		pass

	def delete_cluster(self):
		pass

	def list_clusters_with_details(self):
		pass
    	

