#! /usr/bin/env python3

import argparse
from gcpK8s import GcpK8s

def main(project_id, 
         zone,
         cluster_id):

    gcpK8sInfra = GcpK8s(project_id, zone, cluster_id)

    #gcpK8sInfra.create_cluster()
    
    gcpK8sInfra.list_clusters_with_details()

    gcpK8sInfra.delete_cluster()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.
                                     RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project_id', help='Project ID you want to access.', required=True)
    parser.add_argument('--zone',
                        help='Zone to create clusters in/connect to',
                        required=True)
    parser.add_argument('--cluster_name',
                        help='Name of the cluster to create/connect to',
                        required=True)
    '''
    parser.add_argument('--create_new_cluster',
                        action='store_true',
                        help='States if the cluster should be created')
    parser.add_argument('--global_region',
                        action='store_true',
                        help='If cluster is in the global region')
    '''

    args = parser.parse_args()
    main(args.project_id, args.zone, args.cluster_name)

