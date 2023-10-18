company_id = None

class MultiTenantContextManager:
    def __init__(self, c_id: str) -> None:
        self.c_id = c_id

    def __enter__(self):
        global company_id
        company_id = self.c_id

    def __exit__(self, exc_type, exc_value, exc_traceback):
        global company_id
        company_id = None
        return False


as_company = MultiTenantContextManager

with as_company('My Company'):
    print(company_id)

print(company_id)