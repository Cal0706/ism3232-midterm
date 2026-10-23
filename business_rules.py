
def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Calculate the printing cost before discounts."""
    return copy_price * copies

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Find the discount based on copies and student status."""
    if copies >= 1000:
        discount = 0.15
    elif copies >= 200:
        discount = 0.08
    else:
        discount = 0.0

    if student_org and copies >= 200:
        discount += 0.05

    return discount


def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Calculate the final cost of a printing job."""
    print_cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)

    discounted_cost = print_cost * (1 - discount)

    if discounted_cost < 40:
        discounted_cost += 15

    return round(discounted_cost, 2)


def requires_proof(total: float) -> bool:
    """Check if a printing job needs a proof."""
    return total > 300

def needs_overnight_run(copies: int, total: float) -> bool:
    """Check if a printing job needs an overnight press run."""
    return copies > 500 or total > 400

def total_invoiced(jobs: list) -> float:
    """Add up the total cost of all printing jobs."""
    total = 0.0

    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"],
            job["copies"],
            job.get("student_org", False)
        )
        total += job_total

    return total

def largest_job(jobs: list) -> str:
    """Find the title of the job with the highest total."""
    largest_title = ""
    largest_total = -1

    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"],
            job["copies"],
            job.get("student_org", False)
        )

        if job_total > largest_total:
            largest_total = job_total
            largest_title = job["title"]

    return largest_title

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Format one printing job for the report."""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"

    return f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"









