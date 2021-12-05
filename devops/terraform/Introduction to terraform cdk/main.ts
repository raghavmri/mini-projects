import { Construct } from 'constructs';
import { App, TerraformStack } from 'cdktf';
import { AwsProvider, EC2 } from '@cdktf/provider-aws';

class MyStack extends TerraformStack {
	constructor(scope: Construct, name: string) {
		super(scope, name);
		// define resources here

		new AwsProvider(this, 'aws', {
			region: 'us-east-1',
			accessKey: 'accessKey', // enter your access key here
			secretKey: 'secretKey', // enter your secret key here
		});

		new EC2.Instance(this, 'ec2', {
			instanceType: 't2.micro',
			ami: 'ami-0b9c9f1d',
			availabilityZone: 'us-east-1a',
			keyName: 'my-key-pair',
		});
	}
}

const app = new App({
	outdir: 'dist', // set output directory as your needs
	skipValidation: false, // set to true if you want to skip validation
	stackTraces: false, // set to true if you want to see stack traces
});

const stackName = 'my-stack'; // set stack name as your needs
new MyStack(app, stackName);
app.synth();
