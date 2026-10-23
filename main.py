import business_rules as br

jobs = [
    {"title": "Flyers", "copy_price": 0.25, "copies": 100, "student_org": False},
    {"title": "Menus", "copy_price": 0.50, "copies": 150, "student_org": True},
    {"title": "Posters", "copy_price": 1.20, "copies": 250, "student_org": False},
    {"title": "Programs", "copy_price": 0.80, "copies": 500, "student_org": True},
    {"title": "Catalogs", "copy_price": 0.40, "copies": 2000, "student_org": False},
    {"title": "Banners", "copy_price": 3.00, "copies": 120, "student_org": False},
    {"title": "Tickets", "copy_price": 0.10, "copies": 501, "student_org": False},
    {"title": "Booklets", "copy_price": 1.75, "copies": 300, "student_org": True},
]

print("Brightline Print Shop - Job Report")

for job in jobs:
    total = br.calculate_job_total(job["copy_price"], job["copies"], job["student_org"])

    proof = br.requires_proof(total)
    overnight = br.needs_overnight_run(job["copies"], total)

    print(br.format_job_line(job["title"], total, proof, overnight))

total = br.total_invoiced(jobs)
average = total / len(jobs)

proof_count = 0
overnight_count = 0

for job in jobs:
    job_total = br.calculate_job_total(
        job["copy_price"], job["copies"], job["student_org"]
    )

    if br.requires_proof(job_total):
        proof_count += 1

    if br.needs_overnight_run(job["copies"], job_total):
        overnight_count += 1

print(f"Jobs: {len(jobs)}")
print(f"Total invoiced: ${total:.2f}")
print(f"Average job total: ${average:.2f}")
print(f"Largest job total: {br.largest_job(jobs)}")
print(f"Proofs required: {proof_count}")
print(f"Overnight runs: {overnight_count}")
