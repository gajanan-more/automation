pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run BDD Tests') {
            steps {
                sh 'pytest --gherkin-terminal-reporter --html=reports/test_report.html --self-contained-html'
            }
        }
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/test_report.html', fingerprint: true
            }
        }
    }
}
