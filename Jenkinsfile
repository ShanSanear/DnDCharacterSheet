pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * *')
    }
    options {
        skipDefaultCheckout(true)
        // Keep the 40 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '40'))
        timestamps()
    }
    environment {
      PATH="/var/lib/jenkins/miniconda3/bin:$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Build environment') {
            steps {
                sh '''conda create --yes -n ${BUILD_TAG} python
                      source activate ${BUILD_TAG}
                      pip install -r requirements.txt
                      pip install pylint
                      pip install radon
                      pip install pytest
                      pip install behave
                      pip install behave2cucumber
                      pip install coverage
                      pip install pytest-cov
                      pip install clock
                      pip install pygount
                   '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''source activate ${BUILD_TAG}
                      pip list
                      which pip
                      which python
                    '''
            }
        }
        stage('Static code metrics') {
            steps {
                echo "Raw metrics"
                sh  ''' source activate ${BUILD_TAG}
                        radon raw --json . > raw_report.json
                        radon cc --json . > cc_report.json
                        radon mi --json . > mi_report.json
                        pygount --format=cloc-xml --suffix=py,json --verbose --out cloc.xml
                    '''
                echo "PEP8 style check"
                sh  ''' source activate ${BUILD_TAG}
                        pylint --disable=C,E0611 --output-format=parseable --reports=no  --exit-zero core > core.log
                        pylint --disable=C,E0611 --output-format=parseable --reports=no  --exit-zero gui > gui.log
                        pylint --disable=C,E0611 --output-format=parseable --reports=no  --exit-zero main.py > main.log
                        pylint --disable=C,E0611 --output-format=parseable --reports=no  --exit-zero qt_gui.py > qt_gui.log
                    '''
            }
            post{
                always{
                    recordIssues enabledForFailure: true, tool: pyLint(pattern: '*.log')
                }
            }
        }
        stage('Unit tests') {
            steps {
                sh  ''' source activate ${BUILD_TAG}
                        python -m pytest --verbose --junit-xml test-reports/results.xml
                    '''
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit (allowEmptyResults: true, testResults: 'test-reports/results.xml')
                    sloccountPublish (pattern: 'cloc.xml', commentIsCode: false)
                }
            }
        }
    }
    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}