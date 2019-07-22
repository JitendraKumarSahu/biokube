#! /usr/bin/env python3

from google.cloud import container_v1
import json
from cloud import Cloud

class GcpK8s(Cloud):
	""" GCP Cloud k8s Infrastructure class """
	def __init__(self, project_id, zone, cluster_id):
		self.project_id = project_id
		self.zone = zone
		self.cluster_id = cluster_id
		# [START container_v1_get_client]
		self.client = container_v1.ClusterManagerClient()
		# [END container_v1_get_client]

	# [START container_v1_create_cluster]
	def create_cluster(self):
		"""Create the cluster."""
		print('Creating cluster...')
		with open('k8s_config.json', 'r') as f:
			self.cluster_data = json.load(f)

		self.cluster_data['name'] = self.cluster_id

		self.cluster = self.client.create_cluster(self.project_id, self.zone, 
						self.cluster_data)
	# [END container_v1__create_cluster]

	# [START container_v1__list_clusters_with_detail]
	def list_clusters_with_details(self):
		"""List the details of clusters in the region."""
		print("List the details of clusters in the region.")
		response = self.client.list_clusters(self.project_id, self.zone)
		print (response)
	# [END container_v1__list_clusters_with_detail]

	# [START container_v1__delete]
	def delete_cluster(self):
		"""Delete the cluster."""
		print('Tearing down cluster.')
		result = self.client.delete_cluster(self.project_id, self.zone, self.cluster_id)
		print (result)
	# [END container_v1__delete]

