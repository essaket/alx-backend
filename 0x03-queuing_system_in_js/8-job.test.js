import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    kue.testMode.enter();
  });

  afterEach(() => {
    kue.testMode.clear();
  });

  after(() => {
    kue.testMode.exit();
  });

  it('creates jobs in the queue', () => {
    const jobData = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153518743',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153538781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153118782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4159518782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4158718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153818782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4154318781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4151218782',
          message: 'This is the code 4321 to verify your account'
        }
      ];

    createPushNotificationsJobs(queue, jobData);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_2');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobData[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_2');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobData[1]);
  });
});
