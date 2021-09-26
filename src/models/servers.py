class Server:
    def __init__(self, id, umax):
        self.id = id
        self.umax = umax
        self.running_jobs = []
        self.uptime = 0
        self.can_add_user = True

    def get_id(self):
        return self.id

    def add_job(self, job):
        self.running_jobs.append(job)

    def remove_job(self, job_id):
        job_index = self.running_jobs.index(job_id)
        return self.running_jobs.pop(job_index)

    def get_running_jobs(self):
        return self.running_jobs

    def get_uptime(self):
        return self.uptime

    def update_uptime(self):
        self.uptime += 1
