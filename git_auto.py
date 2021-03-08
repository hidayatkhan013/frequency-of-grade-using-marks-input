
import subprocess as cmd
def git_push_automation():
    try:
        cmd.run("git init", check=True, shell=True)
        cmd.run("git add .", check=True, shell=True)
        cmd.run('git commit -m "first commit"', check=True, shell=True)
        cmd.run("git branch -M main", check=True, shell=True)
        cmd.run('git remote add origin https://github.com/hidayatkhan013/frequency-of-grade-using-marks-input.git', check=True, shell=True)
        cmd.run("git push -u origin main", check=True, shell=True)
        print("Success")
        return True
    except Exception as e:
        print(e)
        return False

git_push_automation()




