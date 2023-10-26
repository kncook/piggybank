from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")
# Rest of your code

app = Flask(__name__)

# Kid class and initialization
class Kid:
    def __init__(self):
        self.savings = 0
        self.savings_goal = 0

    def add_allowance(self, amount):
        self.savings += amount

    def make_purchase(self, cost):
        if cost <= self.savings:
            self.savings -= cost

    def set_savings_goal(self, goal_amount):
        self.savings_goal = goal_amount

    def add_to_savings_goal(self, amount):
        if self.savings_goal > 0:
            if amount <= self.savings:
                self.savings -= amount
                self.savings_goal -= amount

kid = Kid()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "add_allowance" in request.form:
            allowance = float(request.form["allowance"])
            kid.add_allowance(allowance)
        elif "make_purchase" in request.form:
            cost = float(request.form["purchase"])
            kid.make_purchase(cost)
        elif "set_goal" in request.form:
            goal_amount = float(request.form["goal_amount"])
            kid.set_savings_goal(goal_amount)
        elif "add_to_goal" in request.form:
            amount = float(request.form["goal_contribution"])
            kid.add_to_savings_goal(amount)
        return redirect("/")
    return render_template("index.html", kid=kid)

if __name__ == "__main__":
    app.run(debug=True)
