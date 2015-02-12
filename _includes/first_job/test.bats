#!/usr/bin/env bats

@test "wordcount.py counts 35 words" {
    run bash run.sh
    [ $status -eq 0 ]
    [[ ${output} =~ "35" ]]
}
