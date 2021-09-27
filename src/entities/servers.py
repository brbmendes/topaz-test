class Server:
    def __init__(self, id, umax):
        self.id = id
        self.umax = umax
        self.running_jobs = []
        self.uptime = 1
        self.can_add_job = True

    def get_id(self):
        return self.id

    def add_job(self, job):
        self.running_jobs.append(job)
        if len(self.running_jobs) >= self.umax:
            self.can_add_job = False

    def __remove_job(self, job):
        job_index = self.running_jobs.index(job)
        self.running_jobs.pop(job_index)
        if len(self.running_jobs) < self.umax:
            self.can_add_job = True

    def get_running_jobs(self):
        return self.running_jobs

    def get_uptime(self):
        return self.uptime

    def update_uptime(self):
        self.uptime += 1

    def update_tasks_remove_finished(self):
        jobs_to_be_removed = []
        for job in self.running_jobs:
            job.task.ticks -= 1
            if job.task.ticks <= 0:
                jobs_to_be_removed.append(job)

        for job in jobs_to_be_removed:
            self.__remove_job(job)
