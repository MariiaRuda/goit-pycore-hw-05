import sys
import re
from pathlib import Path 
from rich import console
from typing import Optional
from rich.console import Console
from rich.table import Table

def load_logs(path:str)->list:
    with open(path, 'r') as lf:
        return lf.read().splitlines()
        
def parse_log_line(line: str) -> dict:
    date=re.search(r'((\d{4})-(\d{2})-(\d{2}))',line)
    time=re.search(r'((\d{2}):(\d{2}):(\d{2}))',line)
    
    level=re.search(r'(INFO|DEBUG|ERROR|WARNING)',line)
    
    text=re.search(r'(INFO|DEBUG|ERROR|WARNING)\s+(.*)',line)

    line_dict={'date':date.group(1) if date else None,
               'time':time.group(1) if time else None,
               'level':level.group(1) if level else None,
               'text':text.group(2) if text else None}
    return line_dict


def filter_by_logs(logs: list,level:str)->list:
    if level:
        filtered =[l for l in logs if l['level']==level]
        return filtered
    
    
def count_logs_by_level(logs:list)->dict:
    
    count_by_lvl={'INFO': sum([1 for l in logs if l['level']=='INFO']),
     'DEBUG':sum([1 for l in logs if l['level']=='DEBUG']),
     'ERROR':sum([1 for l in logs if l['level']=='ERROR']),
     'WARNING':sum([1 for l in logs if l['level']=='WARNING'])}
    
    return count_by_lvl


if __name__ == "__main__":
    console=Console()
    args=sys.argv
    if len(args)<2:
        console.print(f'[red on red] Please enter a path to file [/]') 
        sys.exit(1)
        
    log_path =sys.argv[1]
    level=sys.argv[2].upper() if len(args)>2 else None
    
    lines=load_logs(log_path) 
    parced_lines=[parse_log_line(line) for line in lines]
    stats=count_logs_by_level(parced_lines)
    
    table=Table(title='[bold magenta underline]LOGS BY LEVEL STATS[/bold magenta underline]')
    table.add_column('Level', style='bold cyan')
    table.add_column('Count', style='bold magenta', justify='right')
    
    for lvl,count in stats.items():
        table.add_row(lvl, str(count))
    console.print(table)
    
    if  level:  
        filtered_by_level=filter_by_logs(parced_lines, level)
        for row in filtered_by_level:
            console.print(row)
    
