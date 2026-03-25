pipeline {
    agent any

    triggers {
        issueCommentTrigger('.*rerun this build.*')
    }

    stages {

        stage('Install') {
            steps {
                echo '[GUARDIAN] Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Dependency Compatibility Tests') {
            steps {
                echo '[GUARDIAN] Running dependency compatibility tests...'
                sh 'python -m pytest test_dependencies.py -v'
            }
        }

    }

    post {
        success {
            echo '[GUARDIAN] ✅ Build PASSED — safe to merge PR'
        }
        failure {
            echo '[GUARDIAN] ❌ Build FAILED — RAG will suggest fix'
        }
    }
}
