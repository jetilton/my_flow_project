from prefect import flow, task

@task
def extract():
    return [1, 2, 3]

@task
def transform(data):
    return [x * 2 for x in data]

@task
def load(data):
    print(f"Loading data: {data}")

@flow
def etl_flow():
    data = extract()
    transformed = transform(data)
    load(transformed)

if __name__ == "__main__":
    etl_flow()
