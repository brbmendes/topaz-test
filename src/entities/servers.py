class Server:
    def __init__(self, id, umax):
        """Creates the Server.

        Keyword arguments:
        id -- the server id
        umax -- max number of simultaneous users connected to the server and running jobs
        """
        self.__id = id
        self.__umax = umax
        self.__running_jobs = []
        self.__uptime = 1
        self.__can_add_job = True

    def get_id(self):
        return self.__id

    def can_add_job(self):
        return self.__can_add_job

    def add_job(self, job):
        if self.__can_add_job:
            self.__running_jobs.append(job)
            if len(self.__running_jobs) >= self.__umax:
                self.__can_add_job = False

    def get_running_jobs(self):
        return self.__running_jobs

    def get_uptime(self):
        return self.__uptime

    def update_uptime(self):
        self.__uptime += 1

    def update_tasks_remove_finished(self):
        jobs_to_be_removed = []
        for job in self.__running_jobs:
            job.get_task().decrement_ticks()
            if job.get_task().get_ticks() <= 0:
                jobs_to_be_removed.append(job)

        for job in jobs_to_be_removed:
            self.__remove_job(job)

    def __remove_job(self, job):
        job_index = self.__running_jobs.index(job)
        self.__running_jobs.pop(job_index)
        if len(self.__running_jobs) < self.__umax:
            self.__can_add_job = True
