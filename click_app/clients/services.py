import csv
import os

from clients.models import Client


class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode="r") as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def updated_client(self, update_client):
        clients_list = self.list_clients()
        update = []
        for client in clients_list:
            if client["uid"] == update_client.uid:
                # lo pasamos como dict porque estamos escribiendo sobre un csv
                update.append(update_client.to_dict())
            else:
                update.append(client)
        self._save_to_disk(update)

    def delete_client(self, del_client):
        clients_list = self.list_clients()
        clients_list.remove(del_client[0])
        self._save_to_disk(clients_list)

    def _save_to_disk(self, clients):
        """
        docstring
        """
        tmp_table_name = self.table_name + ".tmp"
        with open(tmp_table_name, mode="w") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
