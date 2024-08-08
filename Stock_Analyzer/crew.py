from crew import Crew
from agents import Stock_bot_agents 
from task import Stock_bot
from logging import append_event
class Stock_crew:
    def __init__(self,job_id:str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self,stock:str):
        print(f'Crew is working on {stock} with job_id {self.job_id}')
        # Setup Crew
        # Run Crew
        self.crew = Crew(
            agents=[
                Stock_bot_agents.stock_analysis,
            ],
            tasks=[
                Stock_bot.stock_analysis_task,
            ],verbose=True,max_rpm=29
        )
        # Do some work
        print(f'Crew has finished working on {stock}')

    def kickoff_crew(self):
        if not self.crew:
            print(f"No crew setup for job {self.job_id}")
            return 
     
        append_event(self.job_id,"Crew Started")
        try:
            print(f"Running Crew for job {self.job_id}")
            result = self.crew.kickoff()
            append_event(self.job_id,"Crew Finished")
            return result
        except Exception as e:
            append_event(self.job_id,f"Crew Failed: {str(e)}")
            return None