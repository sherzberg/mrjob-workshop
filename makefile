build:
	jekyll build

serve:
	jekyll serve --watch

test:
	cd _includes/first_job/ && bats .
	cd _includes/multistep_job/ && bats .
