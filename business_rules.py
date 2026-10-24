LARGE_ORDER_MIN = 1000
MEDIUM_ORDER_MIN = 200
LARGE_DISCOUNT = 0.15
MEDIUM_DISCOUNT = 0.08
STUDENT_DISCOUNT = 0.05
SETUP_FEE_THRESHOLD = 40
SETUP_FEE = 15
PROOF_THRESHOLD = 300
OVERNIGHT_COPIES_THRESHOLD = 500
OVERNIGHT_TOTAL_THRESHOLD = 400
NO_DISCOUNT = 0.0
ROUND_DECIMALS = 2
DISCOUNT_BASE = 1
INITIAL_LARGEST_TOTAL = -1
INITIAL_TOTAL = 0.0



def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Calculate the printing cost before discounts."""
    return copy_price * copies


def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Find the discount based on copies and student status."""
    if copies >= LARGE_ORDER_MIN:
        discount = LARGE_DISCOUNT
    elif copies >= MEDIUM_ORDER_MIN:
        discount = MEDIUM_DISCOUNT
    else:
        discount = NO_DISCOUNT

    if student_org and copies >= MEDIUM_ORDER_MIN:
        discount += STUDENT_DISCOUNT

    return discount


def calculate_job_total(
    copy_price: float, copies: int, student_org: bool = False
) -> float:
    """Calculate the final cost of a printing job."""
    print_cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)

    discounted_cost = print_cost * (DISCOUNT_BASE - discount)

    if discounted_cost < SETUP_FEE_THRESHOLD:
        discounted_cost += SETUP_FEE

    return round(discounted_cost, ROUND_DECIMALS)


def requires_proof(total: float) -> bool:
    """Check if a printing job needs a proof."""
    return total > PROOF_THRESHOLD


def needs_overnight_run(copies: int, total: float) -> bool:
    """Check if a printing job needs an overnight press run."""
    return copies > OVERNIGHT_COPIES_THRESHOLD or total > OVERNIGHT_TOTAL_THRESHOLD


def total_invoiced(jobs: list) -> float:
    """Add up the total cost of all printing jobs."""
    total = INITIAL_TOTAL

    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job.get("student_org", False)
        )
        total += job_total

    return total


def largest_job(jobs: list) -> str:
    """Find the title of the job with the highest total."""
    largest_title = ""
    largest_total = INITIAL_LARGEST_TOTAL

    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job.get("student_org", False)
        )

        if job_total > largest_total:
            largest_total = job_total
            largest_title = job["title"]

    return largest_title


def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Format one printing job for the report."""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"

    return (
        f"{title}: ${total:.{ROUND_DECIMALS}f} | proof: {proof_text} | overnight run: {overnight_text}"
    )
