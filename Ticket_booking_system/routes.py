class Select_route:

    def __init__(self):
        self.routes = {
            'Kochi to Trivandrum': {'time': '08:00 AM', 'price': 300},
            'Kozhikode to Kochi': {'time': '01:30 PM', 'price': 450},
            'Trivandrum to Palakkad': {'time': '10:00 AM', 'price': 550},
            'Kochi to Bangalore': {'time': '09:00 PM', 'price': 900},
        }
    def display_routes(self):
        s=1
        for k, v in self.routes.items():
            print(f"{s}.{k} - {self.routes[k]["price"]}/- ({self.routes[k]["time"]})")
            s += 1

    def routes_choice(self):
        self.display_routes()
        while True:
            route=int(input("Enter your choice number between 1-4: "))
            if 1<=route and route<=len(self.routes):
                selected_route=list(self.routes.keys())[route-1]
                price_time=self.routes[selected_route]

                return selected_route, price_time
            else:
                print("Invalid choice,enter no between 1-4")

