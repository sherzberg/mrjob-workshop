#!/usr/bin/env bats

@test "wordcount.py counts 35 words" {
    run bash run.sh
    [ $status -eq 0 ]
    [[ ${output} =~ "35" ]]
}

@test "wordcount.py tests pass" {
    run bash python_tests.sh
    [ $status -eq 0 ]
}
