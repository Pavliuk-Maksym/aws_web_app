from flask import Blueprint, render_template

home_bp = Blueprint(
    name="home",
    import_name=__name__,
    template_folder="../templates",
    static_folder="../static",
)


@home_bp.route("/", methods=["GET"])
def home_index():
    return render_template("home.html")
