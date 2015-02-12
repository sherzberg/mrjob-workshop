#!/usr/bin/env bats

@test "multistep counts 18 bats" {
    run bash run.sh
    [ $status -eq 0 ]
    [[ ${output} =~ "18" ]]
    [[ ${output} =~ "bat" ]]
}
