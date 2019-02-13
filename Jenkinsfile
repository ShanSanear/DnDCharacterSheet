pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * *')
    }
    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
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
                        radon raw --json core/ > raw_report.json
                        radon cc --json core/ > cc_report.json
                        radon mi --json core/ > mi_report.json
                        pygount --format=cloc-xml --out cloc.xml --suffix=py --verbose
                    '''
                echo "Code Coverage"
                sh  ''' source activate ${BUILD_TAG}
                        coverage run core/character.py 1 1 2 3
                        python -m coverage xml -o ./reports/coverage.xml
                    '''
                echo "PEP8 style check"
                sh  ''' source activate ${BUILD_TAG}
                        pylint --disable=C core || true
                        pylint --disable=C gui || true
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
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
                }
            }
        }
        stage('integration tests') {
            steps {
                sh  ''' source activate ${BUILD_TAG}
                        behave -f=json.pretty -o ./reports/integration.json
                        python -m behave2cucumber ./reports/integration.json
                    '''
            }
            post {
                always {
                    cucumber (fileIncludePattern: '**/integration*.json',
                              jsonReportDirectory: './reports/',
                              parallelTesting: true,
                              sortingMethod: 'ALPHABETICAL')
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