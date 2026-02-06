class BaseTool:
    def retry(self, fn, retries=3):
        for attempt in range(retries):
            try:
                return fn()
            except Exception as e:
                if attempt == retries - 1:
                    raise e