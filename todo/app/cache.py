import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)


class InvalidLoginAttemptsCache(object):
    @staticmethod
    def _key(email):
        return 'invalid_login_attempt_{}'.format(email)

    @staticmethod
    def _value(lockout_timestamp, timebucket):
        return {
            'lockout_start': lockout_timestamp,
            'invalid_attempt_timestamps': timebucket
        }

    @staticmethod
    def delete(email):
        try:
            cache.delete(InvalidLoginAttemptsCache._key(email))
        except Exception as e:
            logger.exception(e.message)

    @staticmethod
    def set(email, timebucket, lockout_timestamp=None):
        try:
            key = InvalidLoginAttemptsCache._key(email)
            value = InvalidLoginAttemptsCache._value(lockout_timestamp, timebucket)
            cache.set(key, value)
        except Exception as e:
            logger.exception(e.message)

    @staticmethod
    def get(email):
        try:
            key = InvalidLoginAttemptsCache._key(email)
            return cache.get(key)
        except Exception as e:
            logger.exception(e.message)